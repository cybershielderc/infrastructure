import Wrapper from '../layout/Wrapper';
import SEO from '../components/SEO';
import BlogMain from '../components/blogs/blog/';

const Blog = () => {
  return (
    <Wrapper>
      <SEO pageTitle={'Blog Xeco'} />
      <BlogMain/>
    </Wrapper>
  );
};

export default Blog;