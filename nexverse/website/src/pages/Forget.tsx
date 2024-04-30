import Wrapper from '../layout/Wrapper';
import SEO from '../components/SEO';
import RecetPasswordMain from '../components/reset-password';

const RecetPassword = () => {
   return (
      <Wrapper>
         <SEO pageTitle={'Reset PassWord Xeco'} />
         <RecetPasswordMain />
      </Wrapper>
   );
};

export default RecetPassword;