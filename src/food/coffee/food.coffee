# $ ?= require 'jquery' # For Node.js compatibility

add_action = (event_object) -> 
    day_block = $(event_object.target).parent()
    portion = day_block.children('.portions').val()
    day_block.children('ul').append("<li>#{portion}</li>")

$(() ->
    $.get '/food/ajax_portions', (data) ->
      $('.portions').append new Option(i, i, false, false) for i in data
    
    $('.add').click(add_action)
)