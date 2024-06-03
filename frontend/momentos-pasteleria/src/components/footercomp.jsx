import Link from 'next/link';
import Image from 'next/image';
import mainfooterstyle from '../ui/styles/mainfooter.module.css'
import footerLogo from '../ui/img/footer/footerLogo3.png';

export default function FooterMain(){
    return(
        <footer className={mainfooterstyle['footer-main']}>
            <div className={mainfooterstyle['footer-all-content']}>
                <div className={mainfooterstyle['footer-main-container']}>
                    <div>
                        <Image
                            src={footerLogo}
                            alt="catalogo logo"
                        />
                    </div>

                    <div>
                        <h3 className={mainfooterstyle['footer-main-heading']}>CURSOS</h3>
                        <a href='#'> Cursos Online</a>
                        <a href='#'> Cursos Presencial</a>
                    </div>

                    <div>
                        <h3 className={mainfooterstyle['footer-main-heading']}>AYUDA</h3>
                        <a href='#'>Preguntas Frecuentes</a>
                        <a href='#'>Contacto</a>

                    </div>
                </div>

                <div className={mainfooterstyle['footer-bottom-container']}>
                    <span className={mainfooterstyle['footer-bottom-copyright']}>&copy; 2024 Momentos Pasteleria ALL RIGHTS RESERVED. Design by KOLP tech co.</span>
                </div>
            </div>

        </footer>
    )
}