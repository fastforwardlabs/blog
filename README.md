# Install

To update the blog you need to have Hugo and Node.js installed.

## Install Hugo

If you use homebrew run:


```
brew install hugo
```

Otherwise read Hugo's [installation instructions](https://gohugo.io/getting-started/installing).

## Install Node and Node Package Manger

[Read the node installation instructions for your OS](https://nodejs.org/en/download/package-manager/)

## Clone the repo

Clone this repo. It is a large repo because of all the images.

`cd` into the repo and run `npm install`.

# Run the dev environment

After you have everything installed and have made sure your repo is up to date with the latest changes run:

```
npm run dev
```

<img src="https://raw.githubusercontent.com/fastforwardlabs/blog/master/static/images/hugo/shotwin-2020-06-23_15-23-53-1592940260.png" width="600" />

This runs a local version of the blog at `localhost:1313`. It will automatically update as you make changes. It also runs a form that makes it easy to upload images at `localhost:1314`.

# Adding a post

Posts are markdown files with YAML frontmatter. Run the script 

```
s/new_post
```

that will guide you through creating the frontmatter. After you have run through that script you can edit the file it creates in the text editor of your choice. It is standard markdown syntax. Note that we generally use an H5 heading (syntax: `#####`) for image captions. Preview your post on the dev server at `localhost:1313`.

## Uploading an image

<img src="https://raw.githubusercontent.com/fastforwardlabs/blog/master/static/images/hugo/shotwin-2020-06-23_15-23-29-1592940269.png" width="600" />

Go to `localhost:1314` to use a form for uploading an image to use in a post. The page also lists recently uploaded images. Use the relative link shown below the image to add the image in your post, using standard markdown image syntax: `![](relative_link)`. The relative link (no markdown syntax) will also work for the preview image field.

## Publishing your post

To publish your post commit your changes and do `git push origin master`, an automatic Github action will rebuild the site and automatically deploy it. It usually takes around two minutes. You can look under the Github action tab to check its status.

# Adding a prototype link

The prototype section contains links to notebooks and prototypes. It is visible at the bottom of the front page and on its own at https://blog.fastforwardlabs.com/prototypes. To add a prototype add the new entry to the top of `data/prototypes.toml`. Use the previous entries as a guide. The image link can be relative (to an image you added using the process described above) or absolute (to another website) just make sure it is `https` if it is to another site or it won't show up. Look up the TOML format if you have any formatting issues. Just like adding a post, any new entries will be automatically built and deployed after you commit your changes and do `git push origin master`.

# Adding a report link

Adding a link to the report section is similar to adding a prototype link (see above) but it is under `data/reports.toml`. Use previous report entries as your guide.

# Adding a newsletter

We use the blog to generate the newsetter (which is sent through Cloudera marketing ops). Newsletters go here: https://github.com/fastforwardlabs/blog/tree/master/content/newsletters and the html version can be found at URLs like https://blog.fastforwardlabs.com/newsletters/2020-06.html. You also need to inline the CSS (usually we use a Mailchimp tool, maybe someday we'll clean up this process more).

# General info (for debugging)

The main part of the blog is run using Hugo, so the Hugo docs should have most relevant info. Node runs the image upload server (which I (Grant) added to try and make it easier to make posts). The node server files are in the `s` directory, it's a relatively bare-bones node/express app. `npm` is set to run both hugo and the node server through the `package.json` `dev` setting. If you ever want to run hugo only (like if the node part breaks for some reason) you can just use `hugo server`.

The blog is hosted through Github Pages and built using Hugo through Github Actions. Check the "Actions" tab on this repo and read up on Github actions for more info. It's a pretty default 'build Hugo on push' script.
