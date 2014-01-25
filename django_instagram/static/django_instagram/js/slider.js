$(function ()
{
    var slider = $('.django_instagram .slider');
    var slideTag = 'li';
    var transitionTime = 1000;
    var timeBetweenSlides = 6000;

    // Set slider height against absolute positioning
    slider.height($('.django_instagram .entry').height()+'px');

    function slides(i)
    {
        return i >= 0 ? slides().eq(i) : slider.find(slideTag);
    }

    function fadeOut(slide)
    {
        slide.removeClass('active');
        slide.fadeOut(transitionTime);
    }

    function fadeIn(slide)
    {
        slide.addClass('active');
        slide.fadeIn(transitionTime);
    }

    slides().hide();
    fadeIn(slides().first());

    setInterval(function()
    {
        var i = slider.find(slideTag + '.active').index();

        fadeOut(slides(i));

        if (slides().length == i + 1)
            i = -1;

        fadeIn(slides(i + 1));

    }, transitionTime + timeBetweenSlides);
});