#!/usr/bin/env ruby
#
# Check for changed posts
#
# Reads the git history once instead of running git for every post.
# Commits with "[skip lastmod]" in the message (bulk cleanups) are ignored.

LASTMOD_DATES = begin
  dates = {}
  counts = Hash.new(0)
  date = nil

  `git -c core.quotePath=false log --invert-grep -F --grep="[skip lastmod]" --format="@%ad" --date=iso --name-only -- _posts`.each_line do |line|
    line = line.chomp
    next if line.empty?

    if line.start_with?("@")
      date = line[1..]
    else
      counts[line] += 1
      dates[line] ||= date # newest commit comes first
    end
  end

  dates.select { |path, _| counts[path] > 1 }
end

Jekyll::Hooks.register :posts, :post_init do |post|

  path = post.path.delete_prefix("#{post.site.source}/")
  lastmod_date = LASTMOD_DATES[path]

  if lastmod_date
    post.data['last_modified_at'] = lastmod_date
  end

end
