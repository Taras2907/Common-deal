<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Make a Payment</span>
        </v-card-title>
        <v-form ref="form" v-model="valid" :lazy-validation="false">
          <v-card-text>
            <v-container>
              <v-row>
                <v-col cols="12">
                  <v-text-field
                    label="Legal full name"
                    v-model="fullName"
                    :rules="fullNameRules"
                    filled
                    rounded
                    dense
                    outlined
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="cardNumber"
                    filled
                    :rules="cardRules"
                    counter="16"
                    required
                    outlined
                    rounded
                    dense
                    hint="Write here sixteen digits of your card"
                    persistent-hint
                    label="Card number"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                    label="MM/YY"
                    v-model="expirationDate"
                    :rules="expirationDateRules"
                    filled
                    outlined
                    rounded
                    dense
                    hint="Expiration date on the right front corner of card"
                    persistent-hint
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="6">
                  <v-text-field
                    v-model="cvcCode"
                    :rules="cvcRules"
                    filled
                    label="CVC"
                    counter="3"
                    hint="Three digit number on the back side of card"
                    persistent-hint
                    required
                    rounded
                    outlined
                    dense
                  >
                  </v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-form>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="triggerCloseDialog"
            >Cancel</v-btn
          >
          <v-btn
            :disabled="!valid"
            color="blue darken-1"
            text
            @click="triggerSubscribe"
            >Make payment</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  name: "Dialog",
  props: {
    dialog: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      cardNumber: "",
      cardRules: [
        c => !!c || "Card number is required",
        c => /^[0-9]*$/.test(c) || "Only digits required",
        c => (c && c.length === 16) || "Card number must be 16 characters"
      ],

      fullName: "",
      fullNameRules: [n => !!n || "Full name number is required"],

      cvcCode: "",
      cvcRules: [
        c => !!c || "CVC code is required",
        c => /^[0-9]*$/.test(c) || "Only digits required",
        c => (c && c.length === 3) || "CVC code must be 3 characters"
      ],
      expirationDate: "",
      expirationDateRules: [
        d => !!d || "Expiration date is required",
        d => /^[0-9]|\/*$/.test(d) || "Only digits required",
        d =>
          /\d{2}\/\d{2}/.test(d) ||
          "Month and year should have such format MM/YY",
        d =>
          /^([1-9]|1[0-2])\/(2[0-9])$/.test(d) ||
          "Month should be less than 13 and year bigger than 2020"
      ],
      valid: false
    };
  },
  methods: {
    triggerCloseDialog() {
      this.$emit("close-modal");
    },
    triggerSubscribe() {
      this.$emit("subscribe");
    },
    validate() {
      if (this.$refs.form.validate()) {
        this.triggerCloseDialog();
      }
    }
  }
};
</script>

<style scoped></style>
