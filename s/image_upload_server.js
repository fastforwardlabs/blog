let fs = require('fs')
let express = require('express')
let multer = require('multer')
let slugify = require('slugify')
let path = require('path')
let port = 1314

let upload = multer({})

let app = express()

app.post('/post', upload.single('image'), function(req, res, next) {
  let ts = Math.round(new Date().getTime() / 1000)

  // handle image
  let file = req.file
  let image_encoded = req.file.buffer.toString('base64')
  let image_filename = file.originalname.substring(
    0,
    file.originalname.lastIndexOf('.')
  )
  let ext = file.originalname.substring(
    file.originalname.lastIndexOf('.'),
    file.originalname.length
  )
  let new_filename = slugify(image_filename) + '-' + ts + ext

  fs.writeFileSync(
    path.join(__dirname, '../static/images/hugo/' + new_filename),
    req.file.buffer
  )

  setTimeout(() => {
    res.redirect('/')
  }, 1000)
})

app.get('/image_list', (req, res) => {
  let dir = path.join(__dirname, '../static/images/hugo')
  fs.readdir(dir, (err, files) => {
    // sort files
    files = files
      .map(function(fileName) {
        return {
          name: fileName,
          time: fs.statSync(dir + '/' + fileName).ctime.getTime(),
        }
      })
      .sort(function(a, b) {
        return b.time - a.time
      })
      .map(function(v) {
        return v.name
      })

    let html = files
      .map(filename => {
        return `<div><img src="http://localhost:1313/images/hugo/${filename}" /><div>/images/hugo/${filename}</div></div><hr />`
      })
      .join('\n')

    res.send(html)
  })
})

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'server_pages/index.html'))
})

app.listen(port, () =>
  console.log(`Upload server listening at http://localhost:${port}`)
)
