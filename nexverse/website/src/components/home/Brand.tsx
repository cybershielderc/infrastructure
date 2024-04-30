import Slider from "react-slick";

const brand_data: string[] = [
	"/assets/img/brand/brand_img01.png",
	"/assets/img/brand/brand_img02.png",
	"/assets/img/brand/brand_img03.png",
	"/assets/img/brand/brand_img04.png",
	"/assets/img/brand/brand_img05.png",
	"/assets/img/brand/brand_img06.png",
	"/assets/img/brand/brand_img07.png",
];

const settings = {
   dots: false,
	infinite: true,
	speed: 1000,
	autoplay: true,
	arrows: false,
	slidesToShow: 7,
	slidesToScroll: 2,
	responsive: [
		{
			breakpoint: 1200,
			settings: {
				slidesToShow: 5,
				slidesToScroll: 1,
				infinite: true,
			}
		},
		{
			breakpoint: 992,
			settings: {
				slidesToShow: 4,
				slidesToScroll: 1
			}
		},
		{
			breakpoint: 767,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
				arrows: false,
			}
		},
		{
			breakpoint: 575,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1,
				arrows: false,
			}
		},
	]
}

const Brand = () => {
   return (
      <div className="brand-area">
         <div className="container-fluid p-0">
            <div className="row g-0">
               <div className="col-lg-12">
                  <div className="brand-title text-center">
                     <h6 className="title">Our top Partner</h6>
                  </div>
               </div>
            </div>
            <div className="brand-item-wrap">
               <Slider {...settings} className="row g-0 brand-active">
                  {brand_data.map((item, i) => (
                     <div key={i} className="col-12">
                        <div className="brand-item">
                           <img src={item} alt="" />
                        </div>
                     </div>
                  ))}
               </Slider>
            </div>
         </div>
      </div>
   )
}

export default Brand
