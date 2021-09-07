# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name     = "jekyll-wren"
  spec.version  = "0.3"
  spec.authors  = ["Josh Fogg"]
  spec.email    = ["joshua.h.fogg@gmail.com"]

  spec.summary  = "A page-like theme for Jekyll."
  spec.homepage = "https://github.com/Foggalong/Wren"
  spec.license  = "MIT"

  spec.metadata["plugin_type"] = "theme"

  spec.files = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r!^(assets|errors|images|_(includes|layouts|sass)/|(LICENSE|README)((\.(txt|md|markdown)|$)))!i)
  end

  spec.add_runtime_dependency "jekyll", ">= 3.5", "< 5.0"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.9"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.1"

  spec.add_development_dependency "bundler"
end
