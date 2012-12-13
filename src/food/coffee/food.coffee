# $ ?= require 'jquery' # For Node.js compatibility

class Portion
    constructor: (@title, @energy, @proteins, @fats, @carbohydrates) ->

root = exports ? this
root.remove_portion = (event_object) -> 
    $(event_object.target).parent().remove()

add_action = (event_object) -> 
    # define blocks
    meal_block = $(event_object.target).parent()
    info_block = meal_block.parents(".day").children(".info")
    proteins = info_block.children(".proteins");
    fats = info_block.children(".fats");
    carbohydrates = info_block.children(".carbohydrates");
    energy = info_block.children(".energy");

    #get actual portion object
    portion = $.portions[meal_block.children('.portions').val() - 1]

    #add portion to html list
    meal_block.children('ul').append("<li>#{portion.title} <button>x</button></li>")
    $('.food_list li button').click(remove_portion)

    #calculate new values
    new_energy = parseFloat(energy.text()) + portion.energy
    new_proteins = parseFloat(proteins.text()) + portion.proteins
    new_fats = parseFloat(fats.text()) + portion.fats
    new_carbohydrates = parseFloat(carbohydrates.text()) + portion.carbohydrates
    
    #set new values to html elements
    energy.text(new_energy.toFixed(1))
    fats.text(new_fats.toFixed(1))
    proteins.text(new_proteins.toFixed(1))
    carbohydrates.text(new_carbohydrates.toFixed(1))

get_portions = (data) ->
    $.portions = []
    for i in data
       portion = new Portion i.title, i.energy, i.proteins, i.fats, i.carbohydrates
       $.portions.push portion
       $('.portions').append new Option(portion.title, $.portions.length, false, false)
        
$(() ->
    $.getJSON('/food/ajax_portions', get_portions)
    $('.add').click(add_action)
    remove_portion = () ->
        alert('asd')
)