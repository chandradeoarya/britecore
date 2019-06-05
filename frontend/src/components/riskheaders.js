export default [

  {
    name: 'name',
    sortField: 'name',
    title: '<span class="ui teal">Risk Name</span>',
    titleClass: 'center aligned',
    dataClass: 'left aligned'
  },
  {
    name: 'description',
    sortField: 'description',
    title: '<span class="ui teal">Risk Description</span>',
    titleClass: 'center aligned',
    dataClass: 'left aligned'
  },
  {
    name: 'created',
    sortField: 'created',
    title: '<span class="ui teal">Created at</span>',
    titleClass: 'center aligned',
    dataClass: 'center aligned',
    callback: 'formatDate|DD-MM-YYYY HH:mm a'
  },
  {
    name: '__component:custom-action',
    title: 'Actions',
    titleClass: 'center aligned',
    dataClass: 'center aligned'
  }
]
