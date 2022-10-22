$('.slide-items').slick({
    asNavFor:"#text-slider",
    autoplay: true,
    autoplaySpeed: 3000,
    speed: 400
});

$('#text-slider').slick({
    draggable:false,         //ドラッグでのスライド禁止
    arrows:false             //矢印非表示
});