import { Link } from "react-router-dom"
import DocumentForm from "../forms/DocumentForm"

const doc_data: string[] = ["Whitepaper", "Token Sale Terms", "Presentation", "Lightpaper"]

const DocumentArea = () => {
   return (
      <section className="document-area">
         <div className="container">
            <div className="document-inner-wrap">
               <div className="row">
                  <div className="col-lg-12">
                     <div className="section-title text-center mb-60">
                        <h2 className="title">Have Any Questions?</h2>
                     </div>
                  </div>
               </div>
               <div className="row">
                  <div className="col-lg-8">
                     <div className="document-form-wrap">
                        <h4 className="title">Get In Touch Now</h4>
                        <DocumentForm />
                     </div>
                  </div>
                  <div className="col-lg-4">
                     <div className="document-wrap">
                        <h4 className="title">Read Documents</h4>
                        <ul className="list-wrap">
                           {doc_data.map((list, i) => (
                              <li key={i}>
                                 <Link to="#">
                                    <span className="icon"><i className="fas fa-file-pdf"></i></span>
                                    {list}
                                 </Link>
                              </li>
                           ))}
                        </ul>
                        <Link to="#" className="btn">Download All</Link>
                     </div>
                  </div>
               </div>
            </div>
         </div>
         <div className="document-shape">
            <img src="/assets/img/images/document_shape.png" alt="" className="alltuchtopdown" />
         </div>
      </section>
   )
}

export default DocumentArea
