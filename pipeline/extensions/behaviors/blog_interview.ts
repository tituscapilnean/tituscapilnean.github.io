// Blog article pipeline for tituscapilnean.ro: create a stub, voice-interview
// Titus in the browser, lint a draft against his voice rules, and publish the
// finished draft to _posts/. Driven step by step by the blog-factory
// (@swamp/software-factory); each method also works on its own.
import { z } from "npm:zod@4";

const GlobalArgsSchema = z.object({
  blogRepo: z.string().default(
    "/Users/tituspml/Documents/Code/tituscapilnean.github.io",
  ).describe("Absolute path to the blog repo"),
  draftPath: z.string().optional().describe(
    "Legacy: absolute path to one article stub. Methods prefer a slug input.",
  ),
  language: z.string().default("en-US").describe(
    "Speech recognition language, e.g. en-US or ro-RO",
  ),
  port: z.number().int().default(8765),
});

// Every method finds its draft by slug (_drafts/<slug>.md) or by path.
const TargetSchema = z.object({
  slug: z.string().regex(/^[a-z0-9][a-z0-9-]*$/).optional().describe(
    "Article slug; the draft lives at _drafts/<slug>.md",
  ),
  draftPath: z.string().optional().describe("Absolute path to the draft"),
});

const CreateStubArgsSchema = z.object({
  slug: z.string().regex(/^[a-z0-9][a-z0-9-]*$/),
  title: z.string().min(1),
  idea: z.string().min(1).describe("The idea in Titus's own words"),
  categories: z.array(z.string()).default(["English", "AI"]),
  tags: z.array(z.string()).default([]),
});

const AskArgsSchema = TargetSchema.extend({
  question: z.string().min(1).describe("The interview question to ask"),
  timeoutMinutes: z.number().default(30),
});

const LintArgsSchema = TargetSchema.extend({
  postPath: z.string().optional().describe(
    "Lint a published post instead of a draft",
  ),
});

const PublishArgsSchema = TargetSchema.extend({
  date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).describe(
    "Publish date, YYYY-MM-DD (UTC)",
  ),
  postSlug: z.string().regex(/^[a-z0-9][a-z0-9-]*$/).optional().describe(
    "URL slug; defaults to the draft slug without a date prefix",
  ),
});

const StubSchema = z.object({
  slug: z.string(),
  title: z.string(),
  path: z.string(),
  createdAt: z.string(),
});

const AnswerSchema = z.object({
  question: z.string(),
  transcript: z.string(),
  skipped: z.boolean(),
  durationSeconds: z.number(),
  askedAt: z.string(),
  answeredAt: z.string(),
  draftPath: z.string(),
  slug: z.string().optional(),
});

const LintSchema = z.object({
  path: z.string(),
  passed: z.boolean(),
  errors: z.array(z.string()),
  warnings: z.array(z.string()),
  stats: z.object({
    words: z.number(),
    avgSentenceWords: z.number(),
    questionsPer1000: z.number(),
    youPer1000: z.number(),
    h2: z.number(),
    bold: z.number(),
    links: z.number(),
  }),
  checkedAt: z.string(),
});

const PublishedSchema = z.object({
  slug: z.string(),
  postPath: z.string(),
  url: z.string(),
  date: z.string(),
  words: z.number(),
  publishedAt: z.string(),
});

type GlobalArgs = z.infer<typeof GlobalArgsSchema>;
type Target = z.infer<typeof TargetSchema>;

type Context = {
  globalArgs: GlobalArgs;
  writeResource: (
    specName: string,
    name: string,
    data: Record<string, unknown>,
  ) => Promise<{ name: string }>;
  createFileWriter: (
    specName: string,
    name: string,
  ) => { writeAll: (c: Uint8Array) => Promise<{ name: string }> };
  logger: { info: (msg: string) => void };
};

type Submission = {
  transcript: string;
  skipped: boolean;
  durationSeconds: number;
  audio: Uint8Array | null;
};

function resolveDraft(target: Target, globalArgs: GlobalArgs): string {
  if (target.slug) return `${globalArgs.blogRepo}/_drafts/${target.slug}.md`;
  if (target.draftPath) return target.draftPath;
  if (globalArgs.draftPath) return globalArgs.draftPath;
  throw new Error("Pass slug or draftPath");
}

function slugOf(path: string): string {
  return path.split("/").pop()!.replace(/\.md$/, "");
}

const stamp = () => new Date().toISOString().replace(/[:.]/g, "-");

// ---------- create_stub ----------

function stubTemplate(a: z.infer<typeof CreateStubArgsSchema>): string {
  const tags = [...a.tags, '"' + new Date().getUTCFullYear() + '"'];
  return `---
title: ${JSON.stringify(a.title)}
date: ${new Date().toISOString().slice(0, 10)} 12:00:00 +0000
categories: [${a.categories.join(", ")}]
tags: [${tags.join(", ")}]
author: titus
---

> **STUB.** Working notes for the \`titus-blog-voice\` skill. Delete everything above "Draft" before publishing.

## Status

- Stage: idea
- Next step: research and a proposed outline

## The idea (Titus's words)

> ${a.idea.replace(/\n/g, "\n> ")}

## The moment

\`[YOUR MOMENT: the scene that made you want to write this. Never invented.]\`

## Outline

_Not started._

## Open questions

## Research and sources

## Related posts (link, don't repeat)

## Draft

_Not started._
`;
}

// ---------- ask ----------

function page(question: string, language: string): string {
  const q = JSON.stringify(question);
  const lang = JSON.stringify(language);
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blog Interview</title>
<style>
  :root { --bg:#faf9f6; --fg:#1d1d1b; --muted:#6b6a65; --accent:#c2410c; --card:#fff; --line:#e5e3dc; }
  @media (prefers-color-scheme: dark) { :root { --bg:#161614; --fg:#ecebe6; --muted:#9b9a94; --accent:#fb923c; --card:#1f1f1c; --line:#33322e; } }
  * { box-sizing: border-box; }
  body { margin:0; background:var(--bg); color:var(--fg); font:17px/1.5 ui-sans-serif, system-ui, sans-serif; }
  main { max-width:760px; margin:0 auto; padding:48px 16px; }
  .label { color:var(--muted); font-size:13px; letter-spacing:.08em; text-transform:uppercase; }
  h1 { font:600 28px/1.3 ui-serif, Georgia, serif; margin:8px 0 32px; }
  textarea { width:100%; min-height:260px; padding:16px; border:1px solid var(--line); border-radius:10px;
             background:var(--card); color:var(--fg); font:inherit; resize:vertical; }
  .row { display:flex; gap:10px; flex-wrap:wrap; margin:16px 0; align-items:center; }
  button { font:inherit; padding:10px 18px; border-radius:999px; border:1px solid var(--line);
           background:var(--card); color:var(--fg); cursor:pointer; }
  button.primary { background:var(--accent); border-color:var(--accent); color:#fff; }
  button:disabled { opacity:.45; cursor:default; }
  #status { color:var(--muted); font-size:14px; }
  .dot { display:inline-block; width:10px; height:10px; border-radius:50%; background:var(--accent);
         margin-right:6px; animation:pulse 1s infinite; vertical-align:middle; }
  @keyframes pulse { 50% { opacity:.25; } }
  #interim { color:var(--muted); min-height:1.5em; font-style:italic; }
</style></head>
<body><main>
  <div class="label">Interview question</div>
  <h1 id="q"></h1>
  <div class="row">
    <button id="rec" class="primary">Start answering</button>
    <button id="speak">Read question again</button>
    <span id="status"></span>
  </div>
  <div id="interim"></div>
  <textarea id="t" placeholder="Your answer appears here as you talk. Edit anything before you submit."></textarea>
  <div class="row">
    <button id="done" class="primary" disabled>Done, send answer</button>
    <button id="skip">Skip question</button>
  </div>
</main>
<script>
const QUESTION = ${q}, LANG = ${lang};
document.getElementById("q").textContent = QUESTION;
const $ = (id) => document.getElementById(id);
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
let rec = null, media = null, chunks = [], recording = false, started = 0, elapsed = 0;

function speak() {
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(QUESTION);
  u.lang = LANG; u.rate = 1.0;
  speechSynthesis.speak(u);
}
setTimeout(speak, 300);
$("speak").onclick = speak;

if (!SR) $("status").textContent = "Live transcript needs Chrome or Safari. Audio still records; type or paste your answer.";

function startRecognition() {
  if (!SR) return;
  rec = new SR();
  rec.lang = LANG; rec.continuous = true; rec.interimResults = true;
  rec.onresult = (e) => {
    let interim = "";
    for (let i = e.resultIndex; i < e.results.length; i++) {
      const r = e.results[i];
      if (r.isFinal) {
        const t = $("t");
        t.value = (t.value + " " + r[0].transcript.trim()).trim();
      } else interim += r[0].transcript;
    }
    $("interim").textContent = interim;
  };
  rec.onend = () => { if (recording) rec.start(); };
  rec.start();
}

$("rec").onclick = async () => {
  if (!recording) {
    speechSynthesis.cancel();
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      media = new MediaRecorder(stream);
      media.ondataavailable = (e) => e.data.size && chunks.push(e.data);
      media.start(1000);
    } catch (err) { $("status").textContent = "Microphone blocked: " + err.message; return; }
    recording = true; started = Date.now();
    startRecognition();
    $("rec").textContent = "Pause";
    $("status").innerHTML = '<span class="dot"></span>Recording';
    $("done").disabled = false;
  } else {
    recording = false; elapsed += (Date.now() - started) / 1000;
    rec && rec.stop();
    media && media.state !== "inactive" && media.stop();
    media && media.stream.getTracks().forEach((t) => t.stop());
    $("rec").textContent = "Keep talking";
    $("status").textContent = "Paused. Edit the text, keep talking, or send.";
    $("interim").textContent = "";
  }
};

async function send(skipped) {
  if (recording) $("rec").click();
  await new Promise((r) => setTimeout(r, 400));
  const fd = new FormData();
  fd.append("transcript", $("t").value.trim());
  fd.append("skipped", String(skipped));
  fd.append("durationSeconds", String(Math.round(elapsed)));
  if (chunks.length) fd.append("audio", new Blob(chunks, { type: chunks[0].type || "audio/webm" }), "answer.webm");
  $("done").disabled = true; $("skip").disabled = true; $("rec").disabled = true;
  $("status").textContent = "Sending...";
  const res = await fetch("/answer", { method: "POST", body: fd });
  document.querySelector("main").innerHTML = res.ok
    ? '<div class="label">Saved</div><h1>Got it. Back to the terminal for the next question.</h1>'
    : '<div class="label">Error</div><h1>Could not save the answer. Check the terminal.</h1>';
}
$("done").onclick = () => send(false);
$("skip").onclick = () => send(true);
</script></body></html>`;
}

async function waitForAnswer(
  question: string,
  globalArgs: GlobalArgs,
  timeoutMinutes: number,
): Promise<Submission> {
  const abort = new AbortController();
  let resolve!: (s: Submission) => void;
  const answered = new Promise<Submission>((r) => (resolve = r));

  const server = Deno.serve(
    {
      hostname: "127.0.0.1",
      port: globalArgs.port,
      signal: abort.signal,
      onListen: () => {},
    },
    async (req) => {
      const url = new URL(req.url);
      if (req.method === "GET" && url.pathname === "/") {
        return new Response(page(question, globalArgs.language), {
          headers: { "content-type": "text/html; charset=utf-8" },
        });
      }
      if (req.method === "POST" && url.pathname === "/answer") {
        const form = await req.formData();
        const audioField = form.get("audio");
        const audio = audioField instanceof File
          ? new Uint8Array(await audioField.arrayBuffer())
          : null;
        resolve({
          transcript: String(form.get("transcript") ?? ""),
          skipped: form.get("skipped") === "true",
          durationSeconds: Number(form.get("durationSeconds") ?? 0),
          audio,
        });
        return new Response("ok");
      }
      return new Response("not found", { status: 404 });
    },
  );

  await new Deno.Command("open", { args: [`http://127.0.0.1:${globalArgs.port}/`] })
    .output();

  const timeout = new Promise<never>((_, reject) =>
    setTimeout(
      () => reject(new Error(`No answer within ${timeoutMinutes} minutes`)),
      timeoutMinutes * 60_000,
    )
  );
  try {
    return await Promise.race([answered, timeout]);
  } finally {
    abort.abort();
    await server.finished;
  }
}

async function appendToDraft(
  draftPath: string,
  question: string,
  answer: Submission,
  answeredAt: Date,
): Promise<void> {
  const md = await Deno.readTextFile(draftPath);
  const stamp = answeredAt.toISOString().slice(0, 16).replace("T", " ");
  const body = answer.skipped
    ? "_Skipped._"
    : answer.transcript || "_No transcript captured._";
  const entry = `### Q: ${question}\n\n_Answered ${stamp} UTC, ${answer.durationSeconds}s spoken_\n\n${body}\n\n`;

  let next: string;
  if (md.includes("\n## Interview\n")) {
    // Append at the end of the Interview section.
    const start = md.indexOf("\n## Interview\n") + "\n## Interview\n".length;
    const rest = md.slice(start);
    const nextHeading = rest.search(/\n## /);
    const insertAt = nextHeading === -1 ? md.length : start + nextHeading + 1;
    next = md.slice(0, insertAt).trimEnd() + "\n\n" + entry + md.slice(insertAt);
  } else if (md.includes("\n## Draft\n")) {
    const at = md.indexOf("\n## Draft\n") + 1;
    next = md.slice(0, at) + "## Interview\n\n" + entry + md.slice(at);
  } else {
    next = md.trimEnd() + "\n\n## Interview\n\n" + entry;
  }
  await Deno.writeTextFile(draftPath, next);
}

// ---------- lint ----------

const BUZZWORDS = [
  "leverage", "synergy", "unlock", "empower", "transformative",
  "game-changer", "game changer", "revolutionary", "seamless", "robust",
  "cutting-edge", "innovative", "disruptive",
];
const FILLER = [
  /\bit'?s not just\b/i, /\bin a world where\b/i, /\bthe reality is\b/i,
  /\bmake no mistake\b/i, /\bin today'?s world\b/i, /\bas we all know\b/i,
  /\bit goes without saying\b/i, /^here'?s what you need to know/i,
];

function splitPost(md: string): { frontmatter: string; body: string } {
  const m = md.match(/^---\n([\s\S]*?)\n---\n/);
  if (!m) return { frontmatter: "", body: md };
  let body = md.slice(m[0].length);
  const draftAt = body.indexOf("\n## Draft\n");
  if (draftAt !== -1) body = body.slice(draftAt + "\n## Draft\n".length);
  return { frontmatter: m[1], body };
}

function lintText(md: string, path: string): z.infer<typeof LintSchema> {
  const errors: string[] = [];
  const warnings: string[] = [];
  const { frontmatter, body } = splitPost(md);

  md.split("\n").forEach((line, i) => {
    if (/[\u2013\u2014]/.test(line)) {
      errors.push(`line ${i + 1}: em or en dash: ${line.trim().slice(0, 80)}`);
    }
  });

  if (!/^title: .+/m.test(frontmatter)) errors.push("frontmatter: no title");
  const date = frontmatter.match(/^date: (.+)$/m)?.[1] ?? "";
  if (!/\+0000$/.test(date)) errors.push(`frontmatter: date must end in +0000 (${date || "missing"})`);
  if (!/^author: titus$/m.test(frontmatter)) errors.push("frontmatter: author must be titus");
  const tags = frontmatter.match(/^tags: \[(.*)\]$/m)?.[1] ?? "";
  for (const t of tags.split(",").map((s) => s.trim())) {
    if (/^\d{4}$/.test(t)) errors.push(`frontmatter: quote the year tag ${t}`);
  }

  const text = body
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/\[([^\]]*)\]\([^)]*\)/g, "$1")
    .replace(/[#*_>`]/g, " ");
  if (/^\s*_Not started\._\s*$/.test(body.trim()) || text.trim().length === 0) {
    errors.push("draft: no draft text yet");
  }
  if (/\[YOUR MOMENT|STUB\.\*\*/.test(body)) errors.push("draft: placeholder or stub note left in the text");
  const lower = text.toLowerCase();
  for (const w of BUZZWORDS) {
    if (new RegExp(`\\b${w}\\b`).test(lower)) warnings.push(`buzzword: ${w}`);
  }
  for (const re of FILLER) {
    for (const line of text.split("\n")) {
      if (re.test(line.trim())) warnings.push(`filler or inversion: ${line.trim().slice(0, 80)}`);
    }
  }

  const words = (text.match(/[A-Za-z0-9'’]+/g) ?? []).length;
  const sentences = Math.max(1, (text.match(/[.!?](\s|$)/g) ?? []).length);
  const per1000 = (n: number) => (words ? Math.round((n * 10000) / words) / 10 : 0);
  const stats = {
    words,
    avgSentenceWords: Math.round((words / sentences) * 10) / 10,
    questionsPer1000: per1000((text.match(/\?/g) ?? []).length),
    youPer1000: per1000((lower.match(/\byou(r|rs|'re|'ll|'ve)?\b/g) ?? []).length),
    h2: (body.match(/^## /gm) ?? []).length,
    bold: (body.match(/\*\*[^*]+\*\*/g) ?? []).length,
    links: (body.match(/\]\([^)]+\)/g) ?? []).length,
  };
  // Pre-AI baseline: 600 to 1500 words, about 14 "you" and 2.6 questions per 1,000.
  if (words && (words < 600 || words > 1500)) warnings.push(`length: ${words} words (target 600 to 1500)`);
  if (words && stats.youPer1000 < 7) warnings.push(`talks to the reader rarely: ${stats.youPer1000} "you" per 1,000 (baseline about 14)`);
  if (words && stats.questionsPer1000 < 1) warnings.push(`few questions: ${stats.questionsPer1000} per 1,000 (baseline about 2.6)`);
  if (words > 600 && stats.h2 === 0) warnings.push("no H2 sections in a post over 600 words");
  if (stats.bold === 0) warnings.push("no bolded quote line");

  return {
    path,
    passed: errors.length === 0,
    errors,
    warnings,
    stats,
    checkedAt: new Date().toISOString(),
  };
}

// ---------- behavior ----------

export const behavior = {
  type: "@tituscapilnean/blog-interview",
  version: "2026.11.08.2",
  globalArguments: GlobalArgsSchema,
  resources: {
    stub: {
      description: "An article stub created in _drafts/",
      schema: StubSchema,
      lifetime: "infinite",
      garbageCollection: 50,
    },
    answer: {
      description: "One interview question and its transcribed answer",
      schema: AnswerSchema,
      lifetime: "infinite",
      garbageCollection: 50,
    },
    lint: {
      description: "Voice and frontmatter lint results for a draft or post",
      schema: LintSchema,
      lifetime: "infinite",
      garbageCollection: 20,
    },
    published: {
      description: "A draft published to _posts/",
      schema: PublishedSchema,
      lifetime: "infinite",
      garbageCollection: 50,
    },
  },
  files: {
    audio: {
      description: "Raw audio of the spoken answer",
      contentType: "audio/webm",
      lifetime: "infinite",
      garbageCollection: 50,
    },
    archive: {
      description: "The full stub (notes, sources, interview) at publish time",
      contentType: "text/markdown",
      lifetime: "infinite",
      garbageCollection: 50,
    },
  },
  methods: {
    create_stub: {
      description:
        "Create _drafts/<slug>.md from the stub template with the idea in Titus's words. An existing stub is adopted as is, never overwritten.",
      arguments: CreateStubArgsSchema,
      execute: async (
        args: z.infer<typeof CreateStubArgsSchema>,
        context: Context,
      ) => {
        const path = `${context.globalArgs.blogRepo}/_drafts/${args.slug}.md`;
        let existing: string | null = null;
        try {
          existing = await Deno.readTextFile(path);
        } catch (e) {
          if (!(e instanceof Deno.errors.NotFound)) throw e;
        }
        if (existing === null) {
          await Deno.writeTextFile(path, stubTemplate(args));
          context.logger.info(`Created ${path}`);
        } else if (/^---\n[\s\S]*?\n---\n/.test(existing) && existing.includes("\n## Draft\n")) {
          context.logger.info(`Adopted existing stub ${path}`);
        } else {
          throw new Error(`${path} exists but isn't a stub (needs frontmatter and a "## Draft" section)`);
        }
        const handle = await context.writeResource("stub", args.slug, {
          slug: args.slug,
          title: args.title,
          path,
          createdAt: new Date().toISOString(),
        });
        return { dataHandles: [handle] };
      },
    },

    ask: {
      description:
        "Open the question in the browser, read it aloud, record and transcribe the spoken answer, store it, and append it to the draft's Interview section.",
      arguments: AskArgsSchema,
      execute: async (args: z.infer<typeof AskArgsSchema>, context: Context) => {
        const { globalArgs } = context;
        const draftPath = resolveDraft(args, globalArgs);
        await Deno.stat(draftPath);
        const askedAt = new Date();
        context.logger.info(
          `Waiting for your answer at http://127.0.0.1:${globalArgs.port}/`,
        );
        const answer = await waitForAnswer(
          args.question,
          globalArgs,
          args.timeoutMinutes,
        );
        const answeredAt = new Date();
        const id = `qa-${answeredAt.toISOString().replace(/[:.]/g, "-")}`;

        const handles = [
          await context.writeResource("answer", id, {
            question: args.question,
            transcript: answer.transcript,
            skipped: answer.skipped,
            durationSeconds: answer.durationSeconds,
            askedAt: askedAt.toISOString(),
            answeredAt: answeredAt.toISOString(),
            draftPath,
            slug: args.slug ?? slugOf(draftPath),
          }),
        ];
        if (answer.audio && answer.audio.length > 0) {
          handles.push(
            await context.createFileWriter("audio", `audio-${id}`).writeAll(
              answer.audio,
            ),
          );
        }
        await appendToDraft(draftPath, args.question, answer, answeredAt);
        return { dataHandles: handles };
      },
    },

    lint: {
      description:
        "Check a draft's Draft section (or a published post) against the hard voice rules and frontmatter rules, plus pre-AI style stats. Fails when a hard rule is broken.",
      arguments: LintArgsSchema,
      execute: async (args: z.infer<typeof LintArgsSchema>, context: Context) => {
        const path = args.postPath ?? resolveDraft(args, context.globalArgs);
        const result = lintText(await Deno.readTextFile(path), path);
        const handle = await context.writeResource(
          "lint",
          `lint-${slugOf(path)}-${stamp()}`,
          result,
        );
        context.logger.info(
          `${result.stats.words} words, ${result.errors.length} errors, ${result.warnings.length} warnings`,
        );
        for (const w of result.warnings) context.logger.info(`warning: ${w}`);
        if (!result.passed) {
          throw new Error(`Lint failed:\n- ${result.errors.join("\n- ")}`);
        }
        return { dataHandles: [handle] };
      },
    },

    publish: {
      description:
        "Strip the stub's working notes, set the publish date, write _posts/<date>-<slug>.md, archive the full stub as a file, and delete the draft. Refuses if the result fails lint.",
      arguments: PublishArgsSchema,
      execute: async (
        args: z.infer<typeof PublishArgsSchema>,
        context: Context,
      ) => {
        const { blogRepo } = context.globalArgs;
        const draftPath = resolveDraft(args, context.globalArgs);
        const stub = await Deno.readTextFile(draftPath);
        const fm = stub.match(/^---\n[\s\S]*?\n---\n/);
        if (!fm) throw new Error(`No frontmatter in ${draftPath}`);
        const draftAt = stub.indexOf("\n## Draft\n");
        if (draftAt === -1) throw new Error(`No "## Draft" section in ${draftPath}`);

        const frontmatter = fm[0].replace(
          /^date: .*$/m,
          `date: ${args.date} 12:00:00 +0000`,
        );
        const body = stub.slice(draftAt + "\n## Draft\n".length).replace(
          /^\s+/,
          "",
        );
        const post = `${frontmatter}\n${body.trimEnd()}\n`;

        const postSlug = args.postSlug ??
          slugOf(draftPath).replace(/^\d{4}-\d{2}-(\d{2}|xx|zz)-/i, "");
        const postPath = `${blogRepo}/_posts/${args.date}-${postSlug}.md`;
        try {
          await Deno.stat(postPath);
          throw new Error(`Post already exists: ${postPath}`);
        } catch (e) {
          if (!(e instanceof Deno.errors.NotFound)) throw e;
        }

        const check = lintText(post, postPath);
        if (!check.passed) {
          throw new Error(`Not publishing, lint failed:\n- ${check.errors.join("\n- ")}`);
        }

        const archive = await context.createFileWriter(
          "archive",
          `stub-${postSlug}`,
        ).writeAll(new TextEncoder().encode(stub));
        await Deno.writeTextFile(postPath, post);
        await Deno.remove(draftPath);
        context.logger.info(`Published ${postPath}, removed ${draftPath}`);

        const handle = await context.writeResource("published", postSlug, {
          slug: postSlug,
          postPath,
          url: `/posts/${postSlug}/`,
          date: args.date,
          words: check.stats.words,
          publishedAt: new Date().toISOString(),
        });
        return { dataHandles: [handle, archive] };
      },
    },
  },
};
