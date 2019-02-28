library(shiny)
library(magrittr)
library(purrr)
library(httr)

ui <- fluidPage(
  img(src = "https://www.sberbank.ru/portalserver/content/atom/contentRepository/content?id=40d1bd8f-6032-4b89-8824-c431b2adc2a8", style = "margin-top: 1%; width: 300px"),
  titlePanel("Хакатон Сбербанк - Демо"),
  sidebarLayout(
    sidebarPanel(
      textAreaInput("title","Title", placeholder = "Сбербанк",rows = 1),
      textAreaInput("review","Review", placeholder = "Не работает, вылетает!",rows = 5)
    ),
    mainPanel(
      h4("LSTM with Attention layer"),
      htmlOutput("text"),br(),
      
      code("Rating:"),
      htmlOutput("rating",inline = TRUE),br(),
      
      code("Probability"), 
      textOutput("prob", inline = TRUE), br(),br(),
      
      h4("Simple Ridge"),
      htmlOutput("text2"),br(),
      
      code("Rating:"),
      htmlOutput("rating2",inline = TRUE),br()
    )
  ),
  hr(),
  print("Александр Ляшук, НИУ ВШЭ - НН, 4 курс, ИМиКН")
)

server <- function(input, output) {
  observeEvent(c(input$title, input$review),{
    req(nchar(input$title) > 2)
    req(nchar(input$review) > 2)
    
    data <- paste0('http://192.168.88.112:9000/predict/', gsub('[?]','vopros',paste(input$title, input$review))) %>%
      URLencode() %>% 
      GET() %>% 
      content(type = "application/json")
    data$words %<>% transpose() %>% map(simplify) %>% as.data.frame()
    
    s <- ''
    for (row in 1:nrow(data$words)){
      s <- paste0(s, tags$span(data$words[row,"value"], style = paste("background-color: ", data$words[row,"color"])))
      #s <- paste0(s, tags$span(data$words[row,"value"], style = paste("color: ", scales::gradient_n_pal(c("black","red"))( data$words[row,"color"]))))
    }
    
    output$text <- renderText({s})
    output$rating <- renderText({data$class})
    output$prob <- renderText({data$prob})
    
    data2 <- paste0('http://192.168.88.112:9000/predict2/', gsub('[?]','vopros',paste(input$title, input$review))) %>%
      URLencode() %>% 
      GET() %>% 
      content(type = "application/json")
    
    output$text2 <- renderText({data2$words})
    output$rating2 <- renderText({data2$class})
  })
  
}

app <- shinyApp(ui = ui, server = server)
