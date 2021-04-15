window.onscroll = () => {
    const nav = document.querySelector('#navbar');
    if(this.scrollY <= 700) nav.className = ''; else nav.className = 'scroll';
  };