# Install

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

# Adding a post

Posts are markdown files with YAML frontmatter. You can run the script `s/new_post` that will guide you through creating a new post.

## Uploading an image

You can use the script `s/upload` to upload an image to the proper directory and get back a relative link for use in a post.

## Publishing your post

To publish your post `git push origin master`, an automatic Github action will rebuild the site and automatically deploy it. It usually takes around two minutes. You can look under the action tab to check its status.

# Adding a prototype link

The prototype section contains links to notebooks and prototypes. It is visible at the bottom of the front page and on its own at https://blog.fastforwardlabs.com/prototypes. To add a prototype add the new entry to the top of `data/prototypes.toml`. Use the previous entries as a guide. The image link can be relative (to an image you added to the blog) or absolute (to another website) just make sure it is `https` if it is to another site or it won't show up. Look up the TOML format if you have any formatting issues. Just like adding a post, any new entries will be automatically built and deployed after you commit your changes and do `git push origin master`.
