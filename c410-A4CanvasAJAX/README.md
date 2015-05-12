CMPUT410-assignment-ajax
==============================

CMPUT410-assignment-ajax

See requirements.org (plain-text) for a description of the project.

Make a shared state AJAX drawing program

Contributors / Licensing
========================
Daniel Phan Copyright 2015 License extended

Generally everything is LICENSE'D under the Apache 2 license by Abram Hindle.

Resources
===

* HTML Draw Rectangle Canvas
   http://www.html5canvastutorials.com/tutorials/html5-canvas-rectangles/

* Javascript Loops
  http://stackoverflow.com/questions/18238173/javascript-loop-through-json-array 

* Random Color Generator in Javascript:
  http://stackoverflow.com/questions/1484506/random-color-generator-in-javascript
  http://www.paulirish.com/2009/random-hex-color-code-snippets/


Extra
===

This code snippet maybe useful:
    $.ajax ({
        type: "POST",
        url: url,
        data: JSON.stringify(jsonData),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        sucess: function(data){alert(data);},
        failure: function(errMsg) {
            alert(errMsg);
        }
         
    });


