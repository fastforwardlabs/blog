let fs = require('fs')

fs.readdir('posts', function(err, items) {
  for (var i = 0; i < items.length; i++) {
    let item = items[i]
    let oldurl = item
      .replace('-', '/')
      .replace('-', '/')
      .replace('-', '/')
    let first = oldurl.split('.')[0]
    oldurl = first + '.html'
    let alias = 'aliases:\n  - /' + oldurl
    let file = fs.readFileSync('posts/' + item, 'utf-8')
    let exploded = file.split('---')
    exploded[1] = exploded[1] + alias + '\n'
    let content = exploded.join('---')
    fs.writeFileSync(`posts/` + item, content)
  }
})
