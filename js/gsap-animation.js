gsap.registerPlugin(ScrollTrigger);
gsap.config({
    nullTargetWarn: !1,
    trialWarn: !1
});

var $splitone = $('.split_texts').length;

function splitone() {
    if($splitone != ''){
   const split_texts = document.querySelector(".split_texts");
    ScrollTrigger.matchMedia({
        "(min-width: 992px)": function() {
               gsap.to(".split_images", {
  scrollTrigger: {
    trigger: ".ht-img-split-scroller",
    pin: ".split_images",
    scrub: 0.5,
    start: "top top",
    end: () => "+=" + (split_texts.scrollHeight - window.innerHeight),
    id: "ht-img-split-scroller"
  }
});

const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".ht-img-split-scroller",
    start: "top top",
    end: "bottom",
    pin: false,
    scrub: true,
    id: "img"
  }
});
const split_images_blk = gsap.utils.toArray(".split-img-block");
split_images_blk.forEach((img, i) => {
  if (split_images_blk[i + 1]) {
    tl.to(img, { opacity: 0 }, "+=0.2").to(
      split_images_blk[i + 1],
      { opacity: 1 },
      "<"
    );
  }
});
tl.to({}, {}, "+=0.2");
        }
    })  

    };
}


function splittwo() {
  const panels = gsap.utils.toArray(".sticky-panel");
    ScrollTrigger.matchMedia({
        "(min-width: 992px)": function() {
                gsap.to(panels, {
  xPercent: (i) => -100 * i,
  x: (i) => i && 0 * (i - 1),
  duration: (i) => i,
  ease: "none",
  scrollTrigger: {
    trigger: ".sticky-panel-content",
    start: "top top",
    end: "+=" + 100 * panels.length + "5",
    scrub: true,
    pin: true,
  }
});
        }
    }) 
}

function htbgmove() {
  const ht_elm = gsap.utils.toArray('.ht-bg-move-effect');
    if (ht_elm.length == 0) return
    ScrollTrigger.matchMedia({
        "(min-width: 992px)": function() {
            ht_elm.forEach((box, i) => {
                let tl = gsap.timeline({
                    scrollTrigger: {
                        trigger: box,
                        start: "top 80%",
                        end: "+=700px",
                        scrub: 1
                    },
                    defaults: {
                        ease: "none"
                    }
                });
                tl.fromTo(box, {
                    clipPath: 'inset(0% 7% 0% 7%)'
                }, {
                    clipPath: 'inset(0% 0% 0% 0%)',
                    duration: 3
                })
            })
        }
    }) 
};

ScrollTrigger.matchMedia({
    "(max-width: 1200px)": function() {
        ScrollTrigger.getAll().forEach(t => t.kill())
    }
});

jQuery(document).ready(function() {
    splitone();
});
jQuery(window).on('load', function() {
    splitone();
    splittwo();
    htbgmove();
    gsap.delayedCall(1, () => ScrollTrigger.getAll().forEach((t) => {
        t.refresh()
    }))
})