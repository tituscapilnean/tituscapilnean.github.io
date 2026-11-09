# Blog pipeline

Turns an idea into a published post on this blog, in Titus's own voice, through a voice interview. It's a [swamp](https://github.com/swamp-club/swamp) repo inside the blog repo. Jekyll ignores this folder, and changes here don't trigger a deploy.

## Pieces

- **`extensions/behaviors/blog_interview.ts`**: behavior type `@tituscapilnean/blog-interview`, with four methods:
  - `create_stub`: writes `../_drafts/<slug>.md` from the stub template (adopts an existing stub, never overwrites)
  - `ask`: opens an interview question in the browser, reads it aloud, records and transcribes the spoken answer, and appends it to the stub's Interview section
  - `lint`: hard rules (no em or en dashes, `+0000` dates, quoted year tags, `author: titus`, no placeholders) fail the run; buzzwords, filler, length and pre-AI style ratios are warnings
  - `publish`: strips the working notes, sets the date, writes `../_posts/<date>-<slug>.md`, archives the full stub, and deletes the draft
- **`models/@tituscapilnean/blog-interview/blog-pipeline.yaml`**: the behavior every stage calls
- **`models/@swamp/software-factory/blog-factory.yaml`**: the lifecycle, on `@swamp/software-factory`. One work item per post; the work item is the post slug.
- **`agent-constraints/blog-*.md`**: rules for the research, interview, review and publish stages

## The lifecycle

capture, stubbing, research, interview, outline approval (Titus), drafting, adversarial voice review, revising, fact-check, lint, final approval (Titus picks the date), publishing, pull request. Titus merges.

```bash
cd pipeline
swamp extension pull @swamp/software-factory   # once per clone
swamp behavior run blog-factory describe       # render the machine
swamp behavior run blog-factory start --input workItem=<slug>
swamp behavior run blog-factory status --input workItem=<slug>
```

Drive it with the `software-factory` skill (installed by the pull) and the `titus-blog-voice` skill.

## Privacy

Interview transcripts and audio are swamp runtime data under `.swamp/`, which is git-ignored. The blog repo is public; only the code, definitions and stage rules are committed.
