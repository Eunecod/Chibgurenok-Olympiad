<script>
  export default {
    data() {
      return {
        validate: true
      };
    },
    methods: {
      Validate() {
        this.validate = true;
        
        const form_input = this.FindInput(this.$slots.default());
        form_input.forEach((input) => {
          if (!input.dirs[0].value)
            this.validate = false;           
        });
        return this.validate;
      },
      FindInput(nodes) {
        let _nodes = [];
        for (const node of nodes) {
          if (node.type === "input" && (node.props.type === "text" || node.props.type === "password")) { 
            _nodes.push(node);
          }
          if (node.children) {
            _nodes.push(...this.FindInput(node.children));
          }
        }

        return _nodes;
      }
    }
  };
</script>

<template>
  <div id="Validate">
    <slot></slot>
  </div>
</template>
