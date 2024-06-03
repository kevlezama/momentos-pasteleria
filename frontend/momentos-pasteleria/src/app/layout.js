import sytlemainglobal from '../ui/styles/global.module.css'
import PrincipalNavBar from '../components/navbarcomp.jsx'
import FooterMain from '../components/footercomp.jsx'


export const metadata = {
  title: 'Momentos Pasteleria'
}

export default function RootLayout({ children }) {
 return (
    <html className={sytlemainglobal['global-html']} lang="en">
      <body className={sytlemainglobal['global-body']}>
        <PrincipalNavBar/>
        <main className={sytlemainglobal['global-main-container']}>
          {children}
        </main>
        <FooterMain/>
      </body>
    </html>
  )
}
