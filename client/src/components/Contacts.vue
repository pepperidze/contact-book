<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
        <h1>Contacts</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm"
                v-b-modal.contact-add-modal>Add Contact</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Mobile Number</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(contact, index) in contacts" :key="index">
              <td>{{ contact.first_name }}</td>
              <td>{{ contact.last_name }}</td>
              <td>{{ contact.mobile_number }}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm" v-b-modal.contact-edit-modal
                        @click="onUpdate(contact)">Update</button>
                <button type="button" class="btn btn-danger btn-sm"
                        @click="onDelete(contact)">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addContactModal"
            id="contact-add-modal"
            title="Add a new contact"
            hide-footer>
      <b-form @submit="onSubmitAdd" @reset="onResetAdd" class="w-100">
        <b-form-group id="form-first_name-group"
                      label="First Name:"
                      label-for="form-first_name-input">
          <b-form-input id="form-first_name-input"
                        type="text"
                        v-model="addContactForm.first_name"
                        required
                        placeholder="Enter First Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-last_name-group"
                      label="Last Name:"
                      label-for="form-last_name-input">
          <b-form-input id="form-last_name-input"
                        type="text"
                        v-model="addContactForm.last_name"
                        required
                        placeholder="Enter Last Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-mobile_number-group"
                      label="Mobile Number:"
                      label-for="form-mobile_number-input">
          <b-form-input id="form-mobile_number-input"
                        type="text"
                        v-model="addContactForm.mobile_number"
                        required
                        placeholder="Enter Mobile Number">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editContactModal"
            id="contact-edit-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-first_name-edit-group"
                      label="First Name:"
                      label-for="form-first_name-edit-input">
          <b-form-input id="form-first_name-edit-input"
                        type="text"
                        v-model="editContactForm.first_name"
                        required
                        placeholder="Enter First Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-last_name-edit-group"
                      label="Last Name:"
                      label-for="form-last_name-edit-input">
          <b-form-input id="form-last_name-edit-input"
                        type="text"
                        v-model="editContactForm.last_name"
                        required
                        placeholder="Enter Last Name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-mobile_number-edit-group"
                      label="Mobile Number:"
                      label-for="form-mobile_number-edit-input">
          <b-form-input id="form-mobile_number-edit-input"
                        type="text"
                        v-model="editContactForm.mobile_number"
                        required
                        placeholder="Enter Mobile Number">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      contacts: [],
      addContactForm: {
        first_name: '',
        last_name: '',
        mobile_number: '',
      },
      editContactForm: {
        id: '',
        first_name: '',
        last_name: '',
        mobile_number: '',
      },
    };
  },
  methods: {
    getContacts() {
      const path = 'http://localhost:5000/contacts';
      axios.get(path)
        .then((res) => {
          this.contacts = res.data.contacts;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    initForm() {
      this.addContactForm.first_name = '';
      this.addContactForm.last_name = '';
      this.addContactForm.mobile_number = '';
      this.editContactForm.id = '';
      this.editContactForm.first_name = '';
      this.editContactForm.last_name = '';
      this.editContactForm.mobile_number = '';
    },
    addContact(payload) {
      const path = 'http://localhost:5000/contacts';
      axios.post(path, payload)
        .then(() => {
          this.getContacts();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getContacts();
        });
    },
    updateContact(payload, contactID) {
      const path = `http://localhost:5000/contacts/${contactID}`;
      axios.put(path, payload)
        .then(() => {
          this.getContacts();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getContacts();
        });
    },
    removeContact(contactID) {
      const path = `http://localhost:5000/contacts/${contactID}`;
      axios.delete(path)
        .then(() => {
          this.getContacts();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getContacts();
        });
    },
    onSubmitAdd(evt) {
      evt.preventDefault();
      this.$refs.addContactModal.hide();
      const payload = {
        first_name: this.addContactForm.first_name,
        last_name: this.addContactForm.last_name,
        mobile_number: this.addContactForm.mobile_number,
      };
      this.addContact(payload);
      this.initForm();
    },
    onResetAdd(evt) {
      evt.preventDefault();
      this.$refs.addContactModal.hide();
      this.initForm();
    },
    onUpdate(contact) {
      this.editContactForm = contact;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editContactModal.hide();
      const payload = {
        first_name: this.editContactForm.first_name,
        last_name: this.editContactForm.last_name,
        mobile_number: this.editContactForm.mobile_number,
      };
      this.updateContact(payload, this.editContactForm.id);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editContactModal.hide();
      this.initForm();
      this.getContacts();
    },
    onDelete(contact) {
      this.removeContact(contact.id);
    },
  },
  created() {
    this.getContacts();
  },
};
</script>
