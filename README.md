# Blog dev

## Install

The blog is built using Hugo. If you use Homebrew install Hugo with:

```
brew install hugo
```

Otherwise read Hugo's [installation instructions](https://gohugo.io/getting-started/installing).

Clone this repo. `cd` into the repo and run:

```
hugo server
```

This runs a local version of the blog at `localhost:1313`. It will automatically update as you make changes.

## Adding a post

Posts are markdown files with YAML frontmatter. You can run the script `s/new_post` that will guide you through creating a new post.

## Uploading an image

You can use the script `s/upload` to upload an image to the proper directory and get back a relative link for use in a post.

## Publishing your post

To publish your post `git push origin master`, an automatic Github will rebuild the site and automatically deploy it. It usually takes around two minutes. You can look under the action tab to check its status.
