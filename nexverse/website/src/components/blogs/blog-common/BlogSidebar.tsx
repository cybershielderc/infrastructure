import { Link } from "react-router-dom"
import BlogCategory from "./BlogCategory"
import BlogRcPost from "./BlogRcPost"
import BlogTag from "./BlogTag"

const BlogSidebar = () => {
   return (
      <div className="col-lg-4">
         <aside className="blog-sidebar">
            <div className="blog-widget">
               <h4 className="widget-title">Search</h4>
               <div className="sidebar-search">
                  <form onSubmit={(e) => e.preventDefault()}>
                     <input type="text" placeholder="Search your keyword" />
                     <button type="submit"><i className="fas fa-search"></i></button>
                  </form>
               </div>
            </div>
            
            <BlogCategory />
            <BlogRcPost />
            <div className="blog-widget">
               <h4 className="widget-title">Follow Us</h4>
               <div className="sidebar-follow-wrap">
                  <ul className="list-wrap">
                     <li><Link to="#"><i className="fab fa-facebook-f"></i></Link></li>
                     <li><Link to="#"><i className="fab fa-twitter"></i></Link></li>
                     <li><Link to="#"><i className="fab fa-linkedin-in"></i></Link></li>
                     <li><Link to="#"><i className="fab fa-instagram"></i></Link></li>
                  </ul>
                  <Link to="/contact" className="btn">Get In Touch</Link>
               </div>
            </div>
            <BlogTag/>
         </aside>
      </div>
   )
}

export default BlogSidebar
