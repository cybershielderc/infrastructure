"use client"
import { Link } from "react-router-dom";
import Slider from "react-slick";
import team_data from "../../data/TeamData";

const settings ={
   dots: false,
	infinite: true,
	speed: 1000,
    centerMode: true,
    centerPadding: '130px',
	autoplay: false,
	arrows: false,
	slidesToShow: 6,
	slidesToScroll: 1,
	responsive: [
		{
			breakpoint: 1400,
			settings: {
				slidesToShow: 5,
				slidesToScroll: 1,
				infinite: true,
                centerPadding: '70px',
			}
		},
		{
			breakpoint: 1200,
			settings: {
				slidesToShow: 4,
				slidesToScroll: 1,
				infinite: true,
                centerPadding: '40px',
			}
		},
		{
			breakpoint: 992,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 1,
                centerPadding: '0',
                centerMode: false,
			}
		},
		{
			breakpoint: 767,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 1,
				arrows: false,
                centerPadding: '0',
                centerMode: false,
			}
		},
		{
			breakpoint: 575,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1,
				arrows: false,
                centerPadding: '0',
                centerMode: false,
			}
		},
	]
}

const Team = () => {
   return (
      <section className="team-area team-bg" style={{ backgroundImage: `url(/assets/img/bg/team_bg.png)` }}>
         <div className="container-fluid p-0">
            <div className="row g-0">
               <div className="col-12">
                  <div className="section-title text-center mb-50">
                     <h2 className="title">Meet the Brick Veneers</h2>
                  </div>
               </div>
            </div>
            <div className="team-item-wrap">
               <Slider {...settings} className="row team-active g-0">
                  {team_data.map((item) => (
                     <div key={item.id} className="col">
                        <div className="team-item">
                           <div className="team-thumb">
                              <img src={item.img} alt="" />
                              <Link to="#" className="team-social"><i className="fab fa-linkedin-in"></i></Link>
                           </div>
                           <div className="team-content">
                              <h2 className="title">{item.title}</h2>
                              <span>{item.profession}</span>
                           </div>
                        </div>
                     </div>
                  ))}
               </Slider>
               <div className="read-more-btn text-center mt-70">
                  <Link to="/contact" className="btn">All Team Member</Link>
               </div>
            </div>
         </div>
      </section>
   )
}

export default Team
