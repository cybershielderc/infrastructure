import { Link } from "react-router-dom"

const tag: string[] = ["ICO", "blockchain", "investments", "currency", "crypto trading", "crypto", "ico blockchain", "advisor", "web", "ICO Token"]

const BlogTag = () => {
   return (
      <div className="blog-widget">
         <h4 className="widget-title">Tags</h4>
         <div className="sidebar-tag-list">
            <ul className="list-wrap">
               {tag.map((tag, i) => (<li key={i}><Link to="#">{tag}</Link></li>))}
            </ul>
         </div>
      </div>
   )
}

export default BlogTag
