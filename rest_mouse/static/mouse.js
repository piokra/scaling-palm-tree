/**
 * Created by Joanna on 04.10.2016.
 */

String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

function init() {
    $(".left_button").click(left_click);
    $(".right_button").click(right_click);
    $(".click_area").click(mouse_moved);
    $(".click_area").mousemove(mouse_moved);
    $(".left_button").on('touchstart', left_click);
    $(".right_button").on('touchstart', right_click);
    //$(".click_area").on('touchstart', left_click);
    $(".click_area").on('touchmove',mouse_moved );
    $(".click_area").click(left_click);
    $(".click_area").on('contextmenu', right_click_dcm);
}

function left_click() {
    $.post(
        "./api/mouse/",
        JSON.stringify({method: "left"})
    );
}

function right_click() {
    $.post(
        "./api/mouse/",
        JSON.stringify({method: "right"})
    );
}

function right_click_dcm(e) {
	e.preventDefault();
	right_click();
}

function mouse_moved(event) {
    $(".click_area").text("x:{0},  y:{0}".format(event.pageX / $(window).width(), event.pageY / $(window).height()))
    $.post(
        "./api/mouse/",
        JSON.stringify(
            {
                method: "move",
                x: event.pageX / $(window).width(),
                y: event.pageY / ($(window).height() * 0.9)
            }
        )
    )
}

$(document).ready(init);
