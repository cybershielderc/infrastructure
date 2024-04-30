import Wrapper from '../layout/Wrapper';
import SEO from '../components/SEO';
import HomeMain from '../components/home';

const Home = () => {
  return (
    <Wrapper>
      <SEO pageTitle={'Xeco'} />
      <HomeMain/>
    </Wrapper>
  );
};

export default Home;