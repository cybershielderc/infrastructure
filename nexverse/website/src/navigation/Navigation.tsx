import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import Home from '../pages/Home';
import Blog from '../pages/Blog';
import BlogDetails from '../pages/BlogDetails';
import Contact from '../pages/Contact';
import Forget from '../pages/Forget';
import Login from '../pages/Login';
import Register from '../pages/Register';
import ScrollToTop from "../components/common/ScrollToTop";
import { ToastContainer } from "react-toastify";
import DocumentArea from '../components/common/DocumentArea';
import Footer from '../layout/footer/Footer';
import Header from '../layout/headers/Header';
import DynamicBlogDeatils from '../pages/DynamicBlogDetails';

const AppNavigation = () => {

  return (
    <>
      <Router>
        <ScrollToTop />
        <ToastContainer position="top-center" />
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/blog" element={<Blog />} />
          <Route path="/blog-details" element={<BlogDetails />} />
          <Route path="/blog-details/:id" element={<DynamicBlogDeatils />}></Route>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/forgot" element={<Forget />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
        <DocumentArea />
        <Footer />
      </Router>
    </>
  );
};

export default AppNavigation;