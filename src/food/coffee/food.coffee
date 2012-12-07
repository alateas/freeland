# $ ?= require 'jquery' # For Node.js compatibility

add_action = (event_object) -> 
    meal_block = $(event_object.target).parent()
    portion = meal_block.children('.portions').val()
    meal_block.children('ul').append("<li>#{portion}</li>")

get_portions = (portions) ->
    for portion in portions
       $('.portions').append new Option(portion.title, portion.title, false, false)
        
$(() ->
    $.getJSON('/food/ajax_portions', get_portions)
    $('.add').click(add_action)
)