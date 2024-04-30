import { Link } from "react-router-dom"

const Contribution = () => {
   return (
      <section id="contribution" className="contribution-area pt-130 pb-130">
         <div className="container">
            <div className="row justify-content-center">
               <div className="col-lg-10">
                  <div className="contribution-title">
                     <h2 className="title"><span>$45,256,432</span> Contribution Receive</h2>
                  </div>
                  <div className="progress-wrap">
                     <ul className="list-wrap">
                        <li>Pre-Sale</li>
                        <li>soft cap</li>
                        <li>bonus</li>
                     </ul>
                     <div className="progress" role="progressbar">
                        <div className="progress-bar" style={{ width: "83%" }}></div>
                     </div>
                     <h6 className="progress-title"> 65 target raised <span>1 ETH = $1000 = 3177.38 CIC</span></h6>
                  </div>
                  <div className="contribution-btn">
                     <Link to="/contact" className="btn">Purchase a Token</Link>
                     <Link to="/contact" className="btn btn-two">Read White Paper</Link>
                  </div>
               </div>
            </div>
         </div>
         <div className="contribution-shape-wrap">
            <img src="/assets/img/images/contribution_shape01.png" alt="" className="alltuchtopdown" />
            <img src="/assets/img/images/contribution_shape02.png" alt="" className="leftToRight" />
         </div>
      </section>
   )
}

export default Contribution
