<script>
import { Doughnut, mixins } from "vue-chartjs";

const { reactiveProp } = mixins;

export default {
  extends: Doughnut,
  mixins: [reactiveProp],
  // this.chartData is created in the mixin.
  props: [
    // "chartdata",
    "options"
  ],
  mounted() {
    this.renderChart(this.chartData, this.options);
  }
};
</script>

<style lang="scss" scoped></style>
