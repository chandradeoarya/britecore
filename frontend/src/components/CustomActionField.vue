<template>
    <div class="custom-actions">
      <button class="ui basic button" @click="editItem(rowData.id)">edit</button>
      <button class="ui basic button" @click="deleteItem(rowData.id)">delete</button>
      <field-form :popup="popupContent"></field-form>
    </div>
  </template> 
  <script>
  import FieldForm from '@/components/FieldForm'
  import * as types from '@/store/mutation-types.js'

  export default {
    components: {FieldForm},
    props: {
      rowData: {
        type: Object,
        required: true
      },
      rowIndex: {
        type: Number
      }
    },
    data () {
      return {
        popupContent: {
          loading: false,
          mode: 'Edit',
          name: 'field-edit',
          id: this.rowData.id
        }
      }
    },
    methods: {
      editItem (id) {
        this.popupContent.loading = true
        this.$store.commit(types.EDIT_FIELD, id)
        this.$modal.show(this.popupContent.name)
      },
      deleteItem (index) {
        this.$store.dispatch('deleteField', index)
      }
    }
  }
  </script>

  <style>
    .custom-actions button.ui.button {
      padding: 8px 8px;
      font-size: small;
    }
    .custom-actions button.ui.button > i.icon {
      margin: auto !important;
    }
  </style>