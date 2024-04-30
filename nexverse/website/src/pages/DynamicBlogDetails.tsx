import Wrapper from '../layout/Wrapper';
import SEO from '../components/SEO';
import { useParams } from 'react-router-dom';
import useBlogs from '../hooks/UseBlog';
import Breadcrumb from '../components/common/Breadcrumb';
import BlogDetailsArea from '../components/blogs/blog-details/BlogDetailsArea';

const DynamicBlogDeatils = () => {
   const { id } = useParams();
   const { blogs } = useBlogs();
   const blog = blogs.find(blog => Number(blog.id) === Number(id));
   return (
      <Wrapper>
         <SEO pageTitle={'Blog Deatils Xeco'} />
         <Breadcrumb title="Blog Details" />
         <BlogDetailsArea blog={blog} />
      </Wrapper>
   );
};

export default DynamicBlogDeatils;