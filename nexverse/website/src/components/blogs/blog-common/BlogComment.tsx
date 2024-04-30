import { Link } from "react-router-dom"

const BlogComment = () => {
   return (
      <div className="comments-wrap">
         <h3 className="comments-wrap-title">Comments 02</h3>
         <div className="latest-comments">
            <ul className="list-wrap">
               <li>
                  <div className="comments-box">
                     <div className="comments-avatar">
                        <img src="/assets/img/blog/comment01.png" alt="img" />
                     </div>
                     <div className="comments-text">
                        <div className="avatar-name">
                           <h6 className="name">Reed Floren <Link to="#" className="reply-btn">Reply</Link></h6>
                           <span className="date">August 13, 2023</span>
                        </div>
                        <p>The platform itself was incredibly user-friendly, making it easy for me to participate in the ICO. The intuitive interface guided me through the token purchase process seamlessly.</p>
                     </div>
                  </div>
                  
                  <ul className="children list-wrap">
                     <li>
                        <div className="comments-box">
                           <div className="comments-avatar">
                              <img src="/assets/img/blog/comment02.png" alt="img" />
                           </div>
                           <div className="comments-text">
                              <div className="avatar-name">
                                 <h6 className="name">Tony Dargis <Link to="#" className="reply-btn">Reply</Link></h6>
                                 <span className="date">August 15, 2023</span>
                              </div>
                              <p>What stood out to me the most was the exceptional customer support. The team behind the platform was responsive and
                                 helpful, promptly addressing my inquiries and providing.</p>
                           </div>
                        </div>
                     </li>
                  </ul>
               </li>
            </ul>
         </div>
      </div>
   )
}

export default BlogComment
