// Generated by CoffeeScript 1.4.0
(function() {
  var Portion, add_action, get_portions, root;

  Portion = (function() {

    function Portion(title, energy, proteins, fats, carbohydrates) {
      this.title = title;
      this.energy = energy;
      this.proteins = proteins;
      this.fats = fats;
      this.carbohydrates = carbohydrates;
    }

    return Portion;

  })();

  root = typeof exports !== "undefined" && exports !== null ? exports : this;

  root.remove_portion = function(event_object) {
    return $(event_object.target).parent().remove();
  };

  add_action = function(event_object) {
    var carbohydrates, energy, fats, info_block, meal_block, new_carbohydrates, new_energy, new_fats, new_proteins, portion, proteins;
    meal_block = $(event_object.target).parent();
    info_block = meal_block.parents(".day").children(".info");
    proteins = info_block.children(".proteins");
    fats = info_block.children(".fats");
    carbohydrates = info_block.children(".carbohydrates");
    energy = info_block.children(".energy");
    portion = $.portions[meal_block.children('.portions').val() - 1];
    meal_block.children('ul').append("<li>" + portion.title + " <button>x</button></li>");
    $('.food_list li button').click(remove_portion);
    new_energy = parseFloat(energy.text()) + portion.energy;
    new_proteins = parseFloat(proteins.text()) + portion.proteins;
    new_fats = parseFloat(fats.text()) + portion.fats;
    new_carbohydrates = parseFloat(carbohydrates.text()) + portion.carbohydrates;
    energy.text(new_energy.toFixed(1));
    fats.text(new_fats.toFixed(1));
    proteins.text(new_proteins.toFixed(1));
    return carbohydrates.text(new_carbohydrates.toFixed(1));
  };

  get_portions = function(data) {
    var i, portion, _i, _len, _results;
    $.portions = [];
    _results = [];
    for (_i = 0, _len = data.length; _i < _len; _i++) {
      i = data[_i];
      portion = new Portion(i.title, i.energy, i.proteins, i.fats, i.carbohydrates);
      $.portions.push(portion);
      _results.push($('.portions').append(new Option(portion.title, $.portions.length, false, false)));
    }
    return _results;
  };

  $(function() {
    var remove_portion;
    $.getJSON('/food/ajax_portions', get_portions);
    $('.add').click(add_action);
    return remove_portion = function() {
      return alert('asd');
    };
  });

}).call(this);
