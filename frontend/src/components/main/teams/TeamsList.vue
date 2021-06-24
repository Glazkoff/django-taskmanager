<template>
  <v-container>
    <v-row>
      <h1>Список команд</h1>
    </v-row>
    <v-row>
      <v-simple-table width="100%">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">ID</th>
              <th class="text-left">Название команды</th>
              <th class="text-left">Доски</th>
              <th class="text-left">Информация</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="team in teams" :key="team.id">
              <td>{{ team.id }}</td>
              <td>{{ team.name }}</td>
              <td>
                <v-btn
                  v-for="(board, index) in team.boardSet"
                  :key="board.id"
                  color="primary"
                  class="mb-2"
                  :class="{ 'mt-2': index == 0 }"
                  :to="`/board/${board.id}`"
                  >Перейти к доске "{{ board.name }}"</v-btn
                >
              </td>
              <td>{{ team }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-row>
  </v-container>
</template>

<script>
import { TEAMS_LIST } from "@/graphql/queries.js";

export default {
  name: "TeamsList",
  apollo: {
    teams: {
      query: TEAMS_LIST
    }
  }
};
</script>

<style lang="scss" scoped></style>
