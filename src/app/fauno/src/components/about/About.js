import React, { Component } from 'react';
import Menu from '../menu/Menu';
import Footer from '../footer/Footer';

class About extends Component {

	render() {

		return (

			<>
				<Menu />
				<div className="container-fluid">
					<h1 className="text-center">Acerca de</h1>
					<section className="row">
						<article className="col-md-8">

						</article>
					</section>
				</div>
				<Footer />
			</>

		)

	}

}

export default About;