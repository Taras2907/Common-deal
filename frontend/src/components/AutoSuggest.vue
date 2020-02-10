<template>
  <div class="demo">
    <div class="autosuggest-container">
      <vue-autosuggest
        v-model="query"
        :suggestions="filteredOptions"
        @focus="focusMe"
        @click="clickHandler"
        @input="onInputChange"
        @selected="onSelected"
        :get-suggestion-value="getSuggestionValue"
        :input-props="{
          id: 'autosuggest__input',
          placeholder: 'Search for anything'
        }"
      >
        <div
          slot-scope="{ suggestion }"
          style="display: flex; align-items: center;"
        >
          <img
            :style="{
              display: 'flex',
              width: '25px',
              height: '25px',
              borderRadius: '15px',
              marginRight: '10px'
            }"
            :src="suggestion.item.avatar"
          />
          <div :style="{ display: 'flex', color: 'navyblue' }">
            {{ suggestion.item.name }}
          </div>
        </div>
      </vue-autosuggest>
    </div>
  </div>
</template>

<script>
/* eslint-disable */

    import {VueAutosuggest} from "vue-autosuggest";

    export default {
        name: "AutoSuggest",
        components: {
            VueAutosuggest
        },
        data() {
            return {
                query: "",
                selected: "",
                suggestions: [
                    {
                        data: [
                            {
                                id: 1,
                                name: "Frodo",
                                race: "Hobbit",
                                avatar: "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/Elijah_Wood_as_Frodo_Baggins.png/220px-Elijah_Wood_as_Frodo_Baggins.png"
                            },
                            {
                                id: 2,
                                name: "Samwise",
                                race: "Hobbit",
                                avatar: "https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Sean_Astin_as_Samwise_Gamgee.png/200px-Sean_Astin_as_Samwise_Gamgee.png"
                            },
                            {
                                id: 3,
                                name: "Gandalf",
                                race: "Maia",
                                avatar: "https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/Gandalf600ppx.jpg/220px-Gandalf600ppx.jpg"
                            },
                            {
                                id: 4,
                                name: "Aragorn",
                                race: "Human",
                                avatar: "https://upload.wikimedia.org/wikipedia/en/thumb/3/35/Aragorn300ppx.png/150px-Aragorn300ppx.png"
                            }
                        ]
                    }
                ]
            };
        },
        computed: {
            filteredOptions() {
                return [
                    {
                        data: this.suggestions[0].data.filter(option => {
                            return option.name.toLowerCase().indexOf(this.query.toLowerCase()) > -1;
                        })
                    }
                ];
            }
        },
        methods: {
            clickHandler(item) {
                // event fired when clicking on the input
            },
            onSelected(item) {
                this.selected = item.item;
            },
            onInputChange(text) {
                // event fired when the input changes
                console.log(text)
            },
            /**
             * This is what the <input/> value is set to when you are selecting a suggestion.
             */
            getSuggestionValue(suggestion) {
                return suggestion.item.name;
            },
            focusMe(e) {
                console.log(e) // FocusEvent
            }
        }
    }
</script>

<style>
    .demo {
        margin-top: 10px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    }

    #search-content > div {
        font-size: 12px;
        color: gray;
    }

    #search-content:last-child {
        font-size: 10px;
        color: gray;
    }

    #title {
        font-family: 'ZCOOL QingKe HuangYou', cursive;
    }

    #visual {
        font-size: 12px;
        opacity: 80%;
    }

    input {
        border: 2px solid black;
        width: 100%;
        height: auto;
        text-indent: 10px;
    }

    .autosuggest-container {
        display: flex;
        justify-content: center;
        width: auto;
        height: auto;
        margin-top: -10px;
    }

    #autosuggest {
        width: 100%;
        display: block;
    }

    .autosuggest__results > ul {
        width: 100%;
        color: rgba(30, 39, 46, 1.0);
        list-style: none;
        margin: 0;
        padding: 0.5rem 0 .5rem 0;
    }

    .autosuggest__results > ul > li {
        margin: 0 0 0 0;
        border-radius: 5px;
        padding: 0.75rem 0 0.75rem 0.75rem;
        display: flex;
        align-items: center;
    }

    .autosuggest__results > ul > li:hover {
        cursor: pointer;
    }

    .autosuggest__results {
        position: absolute;
        z-index: 1;
        width: 61%;
        background-color: white;

    }

    .autosuggest__results-container {
        width: 100%;
    }

    .autosuggest__results-item--highlighted {
        background-color: rgba(51, 217, 178, 0.2);
    }
</style>