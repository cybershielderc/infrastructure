import { Link } from "react-router-dom";

interface DataType {
   id: number;
   img: string;
   date: string;
   title: string;
}
const rc_data: DataType[] = [
   {
      id: 1,
      img: "/assets/img/blog/rc_post01.jpg",
      date: "July 25,2023",
      title: "We Advocate Swapping Screen Time",
   },
   {
      id: 2,
      img: "/assets/img/blog/rc_post02.jpg",
      date: "July 20,2023",
      title: "Utilizing mobile technology in the field",
   },
   {
      id: 3,
      img: "/assets/img/blog/rc_post03.jpg",
      date: "July 15,2023",
      title: "Building intelligent transportation systems",
   },
]

const BlogRcPost = () => {
   return (
      <div className="blog-widget">
         <h4 className="widget-title">Recent Posts</h4>
         <div className="rc-post-wrap">
            {rc_data.map((item) => (
               <div key={item.id} className="rc-post-item">
                  <div className="thumb">
                     <Link to="/blog-details"><img src={item.img} alt="" /></Link>
                  </div>
                  <div className="content">
                     <span className="date">{item.date}</span>
                     <h6 className="title"><Link to="/blog-details">{item.title}</Link></h6>
                  </div>
               </div>
            ))}
         </div>
      </div>
   )
}

export default BlogRcPost
