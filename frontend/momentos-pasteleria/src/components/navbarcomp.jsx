
/************************************* UI Imports ***************************************/
import navStyles from '../ui/styles/navbar.module.css';
import mpLogo from '../ui/img/logo/mplogo2.png';

/************************************ Nextjs Imports ***********************************/
import Image from 'next/image';
import Link from 'next/link';
import {Button} from "@nextui-org/react";


export default function mainNavBar(){

    return(
        <header className={navStyles['header-main']}>

            <div className={navStyles['header-nav-logo']}>

                <Link href="/"><Image 
                    src={mpLogo}
                    alt="catalogo logo"
                    quality={100}/>
                </Link>

                <nav className={navStyles['header-nav-bar']}>
                    <ul>
                        <li className={navStyles['nav-options-list']}><Link href="/">Home</Link></li>
                        <li className={navStyles['nav-options-list']}><Link href="/aboutus">Nosotros</Link></li>
                        <li className={navStyles['nav-options-list']}><Link href="/courses">Cursos</Link>
                            <ul>
                                <li><Link href="/courses/presentialcourses">Cursos Online</Link></li>
                                <li><Link href="/courses/onlinecourses">Cursos Presencial</Link></li>
                            </ul>
                        </li>
                        <li className={navStyles['nav-options-list']}><Link href="/contact">Contacto</Link></li>
                        <li className={navStyles['nav-options-list']}><Link href="/products">Productos</Link>
                            <ul>
                                <li><Link href="/products/basedetartas">Bases de Tartas</Link></li>
                                <li><Link href="/products/bollerias">Bollerías</Link></li>
                                <li><Link href="/products/budines">Budines</Link></li>
                                <li><Link href="/products/cookies">Cookies</Link></li>
                                <li><Link href="/products/postres">Postres</Link></li>
                            </ul>            
                        </li>
                        
                    </ul>
                </nav>

            </div>
            <div className={navStyles['header-nav-session-buttons']}>
                <div className={navStyles['header-nav-b-contanier']}>  
                    <Button className={navStyles['header-nav-signin-b']}><Link href="/login">Iniciar Sesion</Link></Button>
                </div>
                <div className={navStyles['header-nav-b-contanier']}>
                    <Button className={navStyles['header-nav-login-b']}><Link href="/signin">Registrarse</Link></Button>
                </div>
            </div>
        </header>
    ) 
}