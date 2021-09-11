# frozen_string_literal: true
# Above is a magic comment, telling Ruby all string literals in the file
# are implicitly frozen, as if #freeze had been called on each of them.
# This improves application performance in memory allocation and garbage
# collection. Method's trying to modify strings will raise RuntimeError.

# Tells the Gemfile where to look for gems
source "https://rubygems.org"
gemspec

# In Ruby, '~>' is a twiddle-wakka, or pessimistic version constraint;
# it bounds the last digit below and the second to last digit above.
# For example:
#  * '~>2.2'   means '>= 2.2.0', '< 3.0',
#  * '~>2.2.0' means '>= 2.2.0', '< 2.3.0', etc.
# Use of ~> can also be compounded with >=, !=, etc for complex setups.

# This ensures the current Jekyll version is running
gem "jekyll", "~> 4.2.0"

# If you have any plugins, put them here!
group :jekyll_plugins do
  # gem "jekyll-wren", "~> 0.3"        # Wren from gem install
  gem "jekyll-remote-theme", "~> 0.4"  # Wren remotely from GitHub
  gem "jekyll-feed", "~> 0.12"         # Earliest tested version
  gem "jekyll-seo-tag", "~> 2.1"       # Earliest tested version
  # gem "jekyll-paginate"              # BUG not working
end

# Windows and JRuby do not include zoneinfo files, so bundle the
# tzinfo-data gem and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]
