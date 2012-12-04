# $ ?= require 'jquery' # For Node.js compatibility

add_action = -> $('.food_list').append("<li>#{$('.portions').val()}</li>")

$(() ->
    $.get '/food/ajax', (data) ->
      $('.portions').append new Option(i, i, false, false) for i in data
    
    $('.add').click(add_action)
)