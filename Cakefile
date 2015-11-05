glob = require 'glob'
path = require 'path'
fs   = require 'fs'

markdownSlide = (str)->
  [ 
    "<section data-markdown>"
    str
    "</section>"
  ].join("\n")

task 'compile', ->
  glob './slides/*.md', (err, files)->
    slides = files
      .sort (file, file2)->
        parseInt path.basename(file, '.md') - parseInt path.basename(file2, '.md')
      .map (filename)->
        markdownSlide fs.readFileSync(filename).toString()

    template = fs.readFileSync('./templates/index.html.template').toString()

    fs.writeFileSync "./index.html", template.replace( "{{ SLIDES }}", slides.join('') )
