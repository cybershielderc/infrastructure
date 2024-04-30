import Wrapper from '../layout/Wrapper';
import SEO from '../components/SEO';
import BlogDeatilsMain from '../components/blogs/blog-details';

const BlogDeatils = () => {
  return (
    <Wrapper>
      <SEO pageTitle={'Blog Deatils Xeco'} />
      <BlogDeatilsMain/>
    </Wrapper>
  );
};

export default BlogDeatils;