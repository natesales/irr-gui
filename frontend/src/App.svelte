<script>
  import {
    Content,
    Breadcrumb,
    BreadcrumbItem,
    Grid,
    Row,
    Column,
    Tabs,
    TabContent,
    Tab,
    Select,
    SelectItem,
  } from "carbon-components-svelte";
  import Header from "./components/Header.svelte";
  import Theme from "./components/Theme.svelte";
  import ObjectTable from "./components/ObjectTable.svelte";
  import ObjectForm from "./components/ObjectForm.svelte";
  import {tab} from "./stores";

  let theme = "g10";

  $: {
    if (window.location.hash === "#create") {
      $tab = 1;
    } else if (window.location.hash === "#settings") {
      $tab = 2;
    } else {
      $tab = 0;
      window.location.hash = ""
    }
  }

  $: {
    if ($tab === 0) {
      window.location.hash = "#"
    } else if ($tab === 1) {
      window.location.hash = "#create"
    } else if ($tab === 2) {
      window.location.hash = "#settings"
    }
  }
</script>

<Theme persist bind:theme>
  <Header />
  <Content style="background: none; padding: 1rem">
    <Grid>
      <Row>
        <Column lg="{16}">
          <Breadcrumb noTrailingSlash aria-label="Page navigation">
            <BreadcrumbItem href="/">Home</BreadcrumbItem>
            {#if $tab === 1}
              <BreadcrumbItem href="#create">Create</BreadcrumbItem>
            {:else if $tab === 2}
              <BreadcrumbItem href="#settings">Settings</BreadcrumbItem>
            {/if}
          </Breadcrumb>
          <h1 style="margin-bottom: 1.5rem">View objects</h1>
        </Column>
      </Row>

      <Row>
        <Column noGutter>
          <Tabs aria-label="Tab navigation" bind:selected={$tab}>
            <Tab label="Objects" />
            <Tab label="Create" />
            <Tab label="Settings" />
            <div slot="content" class="tabbed-content">
              <Grid as fullWidth let:props>
                <TabContent {...props}>
                  <Row>
                    <Column>
                      <ObjectTable/>
                    </Column>
                  </Row>
                </TabContent>
                <TabContent {...props}>
                  <Row>
                    <Column>
                      <ObjectForm/>
                    </Column>
                  </Row>
                </TabContent>
                <TabContent {...props}>
                  <Row>
                    <Column md="{4}" lg="{7}">
                      <p>
                        Carbon provides styles and components in Vanilla, React,
                        Angular, Vue and Svelte for anyone building on the web.
                      </p>
                      <br>
                      <Select
                              labelText="Carbon theme"
                              bind:selected="{theme}"
                              style="margin-bottom: 1rem"
                      >
                        <SelectItem value="white" text="White" />
                        <SelectItem value="g10" text="Gray 10" />
                        <SelectItem value="g90" text="Gray 90" />
                        <SelectItem value="g100" text="Gray 100" />
                      </Select>
                    </Column>
                  </Row>
                </TabContent>
              </Grid>
            </div>
          </Tabs>
        </Column>
      </Row>
      <p>&copy; Nathan Sales 2021.</p>
    </Grid>
  </Content>
</Theme>
