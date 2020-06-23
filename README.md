# Install

To update the blog you need to have Hugo and Node.js installed.

### Install Hugo

If you use homebrew run:

```
brew install hugo
```

Otherwise read Hugo's [installation instructions](https://gohugo.io/getting-started/installing).

### Install Node and Node Package Manger

[Read the node installation instructions for your OS](https://nodejs.org/en/download/package-manager/)

### Clone the repo

Clone this repo. It is a large repo because of all the images.

`cd` into the repo and run `npm install`.

# Run the dev environment

After you have everything installed run and have made sure your repo is up to date with the latest changes run:

```
npm run dev
```

This runs a local version of the blog at `localhost:1313`. It will automatically update as you make changes. It also runs a form that makes it easy to upload images at `localhost:1314`.

## Adding a post

Posts are markdown files with YAML frontmatter. Run the script `s/new_post` that will guide you through creating the frontmatter. After you have run through that script you can edit the file it creates in the text editor of your choice. It is standard markdown syntax. Note that we generally use an H5 heading (syntax: `#####`) for image captions. Preview your post on the dev server at `localhost:1313`.

### Uploading an image

Go to `localhost:1314` to use a form for uploading an image to use in a post. The page also lists recently uploaded images. Use the relative link shown below the image to add the image in your post, using standard markdown image syntax: `![](relative_link)`. The relative link (no markdown syntax) will also work for the preview image field.

### Publishing your post

To publish your post commit your changes and do `git push origin master`, an automatic Github action will rebuild the site and automatically deploy it. It usually takes around two minutes. You can look under the Github action tab to check its status.

# Adding a prototype link

The prototype section contains links to notebooks and prototypes. It is visible at the bottom of the front page and on its own at https://blog.fastforwardlabs.com/prototypes. To add a prototype add the new entry to the top of `data/prototypes.toml`. Use the previous entries as a guide. The image link can be relative (to an image you added using the process described above) or absolute (to another website) just make sure it is `https` if it is to another site or it won't show up. Look up the TOML format if you have any formatting issues. Just like adding a post, any new entries will be automatically built and deployed after you commit your changes and do `git push origin master`.
