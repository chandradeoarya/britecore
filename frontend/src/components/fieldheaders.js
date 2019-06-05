export default [

  {
    name: 'name',
    sortField: 'name',
    title: '<span class="ui teal">Field Name</span>',
    titleClass: 'center aligned',
    dataClass: 'left aligned'
  },
  {
    name: 'value',
    sortField: 'value',
    title: '<span class="ui teal">Field Value</span>',
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
    name: '__component:custom-action-field',
    title: 'Actions',
    titleClass: 'center aligned',
    dataClass: 'center aligned'
  }
]
