import { Link } from "react-router-dom"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const Breadcrumb = ({ title }: any) => {
   return (
      <section className="breadcrumb-area breadcrumb-bg" style={{ backgroundImage: `url(/assets/img/bg/breadcrumb_bg.png)` }}>
         <div className="container">
            <div className="row">
               <div className="col-lg-12">
                  <div className="breadcrumb-content">
                     <h2 className="title">{title}</h2>
                     <nav aria-label="breadcrumb">
                        <ol className="breadcrumb">
                           <li className="breadcrumb-item"><Link to="/">Home</Link></li>
                           <li className="breadcrumb-item active" aria-current="page">{title}</li>
                        </ol>
                     </nav>
                  </div>
               </div>
            </div>
         </div>
         <div className="breadcrumb-shape-wrap">
            <img src="/assets/img/images/breadcrumb_shape01.png" alt="" className="alltuchtopdown" />
            <img src="/assets/img/images/breadcrumb_shape02.png" alt="" className="rotateme" />
         </div>
      </section>
   )
}

export default Breadcrumb
