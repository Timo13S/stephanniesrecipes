  // get searchform and page links
  let searchForm = document.getElementById('searchForm')
  let pageLinks = document.getElementsByClassName('page-links')

  // ensure searchform exists
  if(searchForm){
    for(let i=0; pageLinks.length > i; i++)
      pageLinks[i].addEventListener('click',(e)=>{
      e.preventDefault()

      //Get THE DATA ATTRIBUTE
      let page = this.dataset.page

      //ADD HIDDEN SEARCH INPUT TO FORM
      searchForm.innerHTMLm += '<input value=${page} name="page" hidden/>'
      
      //SUBMIT form
      searchForm.submit()
      
    })
  }

