# $ ?= require 'jquery' # For Node.js compatibility

add_action = (event_object) -> alert($(event_object.target).parent) $('.food_list:parent').append("<li>#{$('.portions').val()}</li>")

$(() ->
    $.get '/food/ajax_portions', (data) ->
      $('.portions').append new Option(i, i, false, false) for i in data
    
    $('.add').click(add_action)
)